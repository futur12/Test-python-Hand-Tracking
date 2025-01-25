class GestureMapper:
    def __init__(self):
        pass

    def map_gesture(self, hand_landmarks, mouse_controller):
        # Implémentez la logique pour détecter les gestes spécifiques
        # Exemple : déplacement de la souris avec l'index
        index_finger = hand_landmarks.landmark[8]  # Index
        x, y = int(index_finger.x * 1920), int(index_finger.y * 1080)  # Adapter aux dimensions de l'écran
        mouse_controller.move_mouse(x, y)

        # Ajouter d'autres gestes (clic, clic droit, etc.)