from datetime import datetime

class Workout:
    def __init__(self, workout_type, date, duration, intensity, calories, sets, reps, weight):
        self._date = datetime.strptime(date, "%m-%d-%Y")   
        self.workout_type = workout_type    # Name of workout ex. squats, deadlift
        self.duration = duration    # time in minutes
        self.intensity = intensity  # 1-10
        self.calories = calories    # calories burned
        self.sets = sets
        self.reps = reps
        self.weight = weight    # lbs
    
    def get_summary(self):
        return {
            'date': self._date.strftime('%m-%d-%Y'), 
            'type': self.workout_type,
            'duration': self.duration,
            'intensity': self.intensity,
            'calories': self.calories,
        }
    
    def _format_date(self):
        return self._date.strftime("%B %d, %Y")

    def __str__(self):
        return (f"{self._format_date()} - {self.workout_type} | {self.sets}x{self.reps} @ {self.weight} lbs for {self.duration} min | Intensity: {self.intensity}/10 | Calories Burned: {self.calories}")
    

    def __lt__(self, other):
        return self._date < other._date
    

    def __eq__(self, other):
        return (self.workout_type == other.workout_type and self.duration == other.duration and self.sets == other.sets and self.reps == other.reps)
    
    

    
    
