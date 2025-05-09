from workout import Workout

def test_str():
    w = Workout("Squat", "04-01-2025", 45, 8, 350, 4, 8, 185)
    assert "Squat" in str(w)

def test_comparison():
    w1 = Workout("Deadlift", "03-30-2025", 50, 9, 400, 2, 6, 225)
    w2 = Workout("Deadlift", "04-01-2025", 50, 9, 400, 3, 6, 225)
    assert w1 < w2

def test_equality():
    w1 = Workout("Pushups", "04-01-2025", 30, 5, 150, 3, 10, 0)
    w2 = Workout("Pushups", "04-01-2025", 30, 5, 150, 3, 10, 0)
    assert w1 == w2

test_str()
test_comparison()
test_equality()
print("All tests passed!")
