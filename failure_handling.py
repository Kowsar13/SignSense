try:
    lcd.message("ALARM DETECTED")
except Exception as e:
    print("LCD error:", e)
    try:
        tts_engine.say("Alarm detected")
        tts_engine.runAndWait()
    except Exception as e:
        print("TTS error:", e)
        # fallback to vibration motor
        GPIO.output(VIBRATION_PIN, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(VIBRATION_PIN, GPIO.LOW)
