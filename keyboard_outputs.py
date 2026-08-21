import keyboard 
import time

last_p = 0
last_b = ""
MINIMUM_FOR_D = 0.3
MODIFICTAORS = ["ctrl", "alt", "shift", "windows"]
def get_modificators():
    active = []
    for mod in MODIFICTAORS:
        if keyboard.is_pressed(mod):
            active.append(mod)
    return active 

def keys_pressed(event):
    global last_p, last_b
    curreen_t = time.time()
    key_n = event.name.lower()
    active_mods = get_modificators()
    if active_mods and key_n not in active_mods:
        combo = "+".join(active_mods + [key_n])
        print(f"combination '{combo.upper()}' was pressed!")
        last_p = 0
        last_b = ""
    print(f"key {key_n} was pressed")
    if(key_n == last_b and (curreen_t - last_p) < MINIMUM_FOR_D):
        print(f"WARNING!: Button '{key_n.upper()}' was double clicked!")
        last_p = 0
        last_b = ""
    else:
        last_p = curreen_t
        last_b = key_n
keyboard.on_press(keys_pressed)
print("Waiting for input...")
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        pass 