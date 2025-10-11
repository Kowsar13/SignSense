def gpio_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_PIN, GPIO.OUT, initial=GPIO.LOW)

def vibrate_async(sec: float = 3.0):
    def run():
        GPIO.output(MOTOR_PIN, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(MOTOR_PIN, GPIO.LOW)
    threading.Thread(target=run, daemon=True).start()

def lcd_updater(stop_flag):
    while not stop_flag["stop"]:
        line1 = (last_sign.get("text") or "").strip()[:16]
        line2 = (last_sound.get("text") or "").strip()[:16]
        lcd.home(); lcd.write_string(line1.ljust(16)); lcd.crlf()
        lcd.write_string(line2.ljust(16))
        time.sleep(1)
