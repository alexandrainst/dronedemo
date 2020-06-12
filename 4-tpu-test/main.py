import argparse
from edgetpu.detection.engine import DetectionEngine
import PIL
import base64
from io import BytesIO
import cv2

import time 
from collections import deque
time_queue = deque([])

width, height = 640,480

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='Path of the detection model.', required=True)
    
    args = parser.parse_args()    

    engine = DetectionEngine(args.model)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    print("Camera started. Streaming results")    
    
    while(cap.isOpened()):
        print("Running")
        _, frame = cap.read()
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(im)

        ans = engine.detect_with_image(img, threshold = 0.35, keep_aspect_ratio = True, relative_coord= False, top_k = 1) 
        
        pred = "nopeople"
        pos = 1.0
 
        if ans:
            for obj in ans:
                if (obj.label_id==0):
                    box = obj.bounding_box.flatten().tolist()

                    pos =  ((box[0]+box[2])/width) - 1
                    pred = '{:.3f}'.format(pos)
                    print(pos)
        
        print(pos)
        print(pred)
      
        time_queue.append(time.time()) 
        if len(time_queue) > 5:
            time_queue.popleft()
         
        if len(time_queue) > 1:
           print("FPS: ", len(time_queue)/(time_queue[-1]-time_queue[0]))   
 
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

if __name__ == '__main__':
    main()
