import pynput.keyboard as Keyboard
import os,sys

def on_press(key):
    # Callback function whenever a key is pressed
    try:
        print(f'Key {key.char} pressed!')
        #file= open('key.txt','a')
        #file.write(str(key.char))
        #print(end='\n')
        #file.close()
    except AttributeError:
        print(f'Special Key {key} pressed!')
        #file = open('key.txt', 'a')
        #file.write(str(key))
        #print(end='\n')
        #file.close()

#def on_release(key):
 #   print(f'Key {key} released')
  #  if key == Keyboard.Key.esc:
   #     # Stop the listener
    #    return False


with Keyboard.Listener(on_press=on_press) as listener:
    listener.join()

if __name__ == '__main__':
    on_press()
    #on_release()