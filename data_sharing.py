import random, logging
from multiprocessing import Process, Manager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(processName)s - %(levelname)s - %(message)s')

def extract_radius(q1, q2):
    for i in range(5):
        circum = q1.get()
        radius = circum/(2*3.14159)
        logging.info(f"Extracted radius {radius} from circumference {circum}")
        q2.put(radius)

def calculate_area(q):
    for i in range(5):
        radius = q.get()
        area = radius**2 * 3.14159
        logging.info(f"Calculated area {area} from radius {radius}")

def send_circumfrence(q):
    for i in range(5):
        circum = random.randint(5,50)
        q.put(circum)
        logging.info(f"Sent circumfrence {circum}")
def perform_operations():
    q1,q2 = Manager().Queue(),Manager().Queue()
    p1,p2,p3 = Process(target=send_circumfrence, args=(q1,)), Process(target=extract_radius, args=(q1, q2,)), Process(target=calculate_area, args=(q2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
