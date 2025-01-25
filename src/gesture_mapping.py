class GestureMapper:
    def __init__(self):
        pass

#  def maps(self, hand_landmarks, mouse_controller):
    def map_gesture(self, hand_landmarks, mouse_controller):
        # Coordonnées des points clés
        index_finger_tip = hand_landmarks.landmark[8]  # Index
        thumb_tip = hand_landmarks.landmark[4]  # Pouce

        # Adapter les coordonnées à la taille de l'écran
        x, y = int(index_finger_tip.x * 1920), int(index_finger_tip.y * 1080)
        mouse_controller.move_mouse(x, y)

        # Distance entre le pouce et l'index
        thumb_index_distance = self._calculate_distance(thumb_tip, index_finger_tip)

        # Détection des gestes
        if thumb_index_distance < 0.05:  # Ajustez la valeur selon la précision requise
            mouse_controller.click()  # Clic gauche
        elif thumb_index_distance > 0.05 and thumb_index_distance < 0.1:  # Exemple de condition pour clic droit
            mouse_controller.right_click()

    @staticmethod
    def _calculate_distance(point1, point2):
        """Calcule la distance entre deux points."""
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
