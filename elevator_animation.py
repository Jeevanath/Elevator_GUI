import tkinter
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('secret_key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://lift-gui-default-rtdb.firebaseio.com/"
})

ref = db.reference('LIFTS')
print(ref.get())


Window_Width=1200

Window_Height=600


Refresh_Sec = 0.001





def create_animation_window():
  Window = tkinter.Tk()
  Window.title("Elevator monitoring")
  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window
 

def create_animation_canvas(Window):
  canvas = tkinter.Canvas(Window)
  canvas.configure(bg="black")
  canvas.pack(fill="both", expand=True)
  return canvas


def draw_lift(Lift):
  Lift = Animation_canvas.create_rectangle(Lift.x_min, Lift.y_min, Lift.x_max, Lift.y_min - 100, fill = 'grey')
  return Animation_canvas


Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)



class Lifts:
  def __init__(self, name, x_min, y_min, x_max):
    self.name = name
    self.x_min = x_min
    self.y_min = y_min
    self.x_max = x_max
    Animation_canvas.create_text(x_min + 15, 50, text = name, fill = 'white', font=('Helvetica 15 bold'))
    





# class Floor:
#   def draw(name, x_min, y_min, x_max, y_max, Animation_canvas):

#    name = Animation_canvas.create_line(x_min, y_min, x_max, y_max, fill='white', width=5)
#    return Animation_canvas




class Floor:
  def __init__(self, name, x_min, y_min, x_max, y_max):
    self.name = name
    self.x_min = x_min
    self.y_min = y_min
    self.x_max = x_max
    self.y_max = y_max
    Animation_canvas.create_line(x_min, y_min, x_max, y_max, fill='white', width=10)
    Animation_canvas.create_text(x_min + 15, y_min - 15, text = name, fill = 'white', font=('Helvetica 15 bold'))

   
   




LiftA = Lifts("LiftA", 500, 600, 550)
LiftB = Lifts("LiftB", 700, 600, 750)









F1 = Floor("2F", 0, 200, 50, 200)
F2 = Floor("1F", 0, 400, 50, 400)
GF = Floor("GF", 0, 600, 50, 600)






print(Animation_canvas.coords(F1))















def animate_Lift(Window, canvas, LiftA, LiftB):

 LiftA = canvas.create_rectangle(LiftA.x_min, LiftA.y_min, LiftA.x_max, LiftA.y_min - 100, fill = 'grey')
 LiftB = canvas.create_rectangle(LiftB.x_min, LiftB.y_min, LiftB.x_max, LiftB.y_min - 100, fill = 'grey')




 while True:
  LiftA_pos = canvas.coords(LiftA)
  x1, y1, x2, y2 = LiftA_pos


  Lifts_dict = ref.get()
  
  if y2 < Lifts_dict['LiftA'] * (-200) + 600:
    canvas.move(LiftA,0,10)

  if y2 > Lifts_dict['LiftA'] * (-200) + 600:
    canvas.move(LiftA,0,-10)

  Window.update()
  time.sleep(Refresh_Sec)
 
 


animate_Lift(Animation_Window,Animation_canvas, LiftA, LiftB)