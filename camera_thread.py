def camera_thread(stop_flag):
    cap = open_camera()
    hands = mp.solutions.hands.Hands(max_num_hands=1)
    while not stop_flag["stop"]:
        ok, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = hands.process(rgb)
        if res.multi_hand_landmarks:
            hand = res.multi_hand_landmarks[0]
            xvec = make_feature_vector(hand, EXPECTED_DIM)
            idx, conf = gesture_predict(xvec)
            if conf >= CONF_THRESHOLD_SIGN:
                last_sign.update({"text": id_to_label.get(idx, str(idx)), "conf": conf})
