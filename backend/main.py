from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json
import pyautogui

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ALPHA = 0.2
prev_x, prev_y = 0.5, 0.5
pyautogui.FAILSAFE = False

# Screen size detection for cursor mapping
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global prev_x, prev_y
    await websocket.accept()
    print("Backend: Connection Accepted!")
    try:
        while True:
            data = await websocket.receive_text()
            coords = json.loads(data)
            
            raw_x = coords.get("x", 0.5)
            raw_y = coords.get("y", 0.5)
            action = coords.get("action", "move") # Naya field for click detection

            # Mirroring and Smoothing
            target_x = 1 - raw_x 
            target_y = raw_y

            curr_x = (ALPHA * target_x) + (1 - ALPHA) * prev_x
            curr_y = (ALPHA * target_y) + (1 - ALPHA) * prev_y
            prev_x, prev_y = curr_x, curr_y

            # --- System Control Block ---
            # Map normalized (0-1) coordinates to screen pixels
            mouse_x = curr_x * SCREEN_WIDTH
            mouse_y = curr_y * SCREEN_HEIGHT
            
            # Move the system cursor
            pyautogui.moveTo(mouse_x, mouse_y, _pause=False)

            # Trigger click if action is sent from frontend
            if action == "click":
                pyautogui.click()
                print("Action: Left Click Executed")
            # ----------------------------

            await websocket.send_json({
                "status": "success",
                "x": round(curr_x, 4),
                "y": round(curr_y, 4),
                "executed_action": action
            })
    except Exception as e:
        print(f"WS Error: {e}")