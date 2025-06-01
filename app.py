<!DOCTYPE html>
<html>
<head>
    <title>Antibiotic Resistance Predictor</title>
</head>
<body>
    <h1>Antibiotic Resistance Predictor</h1>

    <h2>Enter Genome Features:</h2>
    <form id="predictForm">
        <input type="number" step="any" name="f1" placeholder="Feature 1"><br>
        <input type="number" step="any" name="f2" placeholder="Feature 2"><br>
        <input type="number" step="any" name="f3" placeholder="Feature 3"><br>
        <!-- Add more inputs based on model needs -->
        <button type="submit">Predict</button>
    </form>

    <h3 id="result"></h3>

    <script>
        const form = document.getElementById('predictForm');
        const result = document.getElementById('result');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const features = Array.from(formData.values()).map(Number);

            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ features })
            });

            const data = await response.json();

            if (data.error) {
                result.textContent = `Error: ${data.error}`;
            } else {
                result.textContent = `Prediction: ${data.interpretation} (Probability: ${data.probability.toFixed(2)})`;
            }
        });
    </script>
</body>
</html>
