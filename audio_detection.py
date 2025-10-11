def classify_audio(buf16k: np.ndarray):
    xin = adapt_audio_for_model(buf16k)
    a_itp.set_tensor(IN_INDEX, xin)
    a_itp.invoke()
    probs = a_itp.get_tensor(a_out_det["index"])
    cls  = int(np.argmax(probs))
    conf = float(np.max(probs))
    disp = sound_display_map.get(cls, "")
    return cls, disp, conf
