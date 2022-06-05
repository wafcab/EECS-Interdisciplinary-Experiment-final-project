from image_classify import run as image
from audio_classify import run as audio
from toESP_Arduino import ESP_close, ESP_connect

def main():
      addr = input("Please enter the Server ip:")
      ESP_connect(addr)
      input_source = 'Image'
      while True:
            if input_source == 'Image':
                  #@ image(model, maxResults, numThreads, enableEdgeTPU, cameraId, frameWidth, frameHeight)
                  input_source = image('image_model_metadata.tflite', 5, 4, False, 0, 640, 480)
            if input_source == 'Audio':
                  #@ audio(model, max_results, score_threshold, overlapping_factor, num_threads, enable_edgetpu) 
                  input_source = audio('audio_model_metadata.tflite', 5, 0.0, 0.5, 4, False)
            if input_source == 'ESC':
                  #@ end the program when pressing key ESC
                  ESP_close()
                  print('Escape!'+'-'*30)
                  break

if __name__ == '__main__':
  main()