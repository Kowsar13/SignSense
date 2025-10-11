def audio_thread(stop_flag):
    MIC_SR = 48000
    sd.default.samplerate = MIC_SR
    sd.default.channels = 1
    ring = []
    def cb(indata, frames, time_info, status):
        ring.append(np.squeeze(indata).astype(np.float32))
    with sd.InputStream(callback=cb, dtype='float32'):
        while not stop_flag["stop"]:
            if not ring: continue
            buf = np.concatenate(ring)[-int(MIC_SR*AUDIO_WIN_SEC):]
            clip = resample_to_16k(buf, MIC_SR)
            cls, name, conf = classify_audio(clip)
            if conf >= CONF_THRESHOLD_AUDIO and cls in EMERGENCY_IDX:
                last_sound.update({"text": name, "conf": conf})
                vibrate_async(3.0)
                speak_guarded(name)
            ring.clear()
