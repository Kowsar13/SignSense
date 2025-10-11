def build_tflite(path: str) -> Interpreter:
    
    try:
        itp = Interpreter(model_path=path, num_threads=2)
    except TypeError:
        itp = Interpreter(model_path=path)
    itp.allocate_tensors()
    return itp

g_itp = build_tflite(GESTURE_TFLITE)
g_in_det  = g_itp.get_input_details()[0]
g_out_det = g_itp.get_output_details()[0]
g_in  = g_in_det["index"]
g_out = g_out_det["index"]