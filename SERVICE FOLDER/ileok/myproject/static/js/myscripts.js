const form = document.querySelector('form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Show loading text and start updating it
    const loadingDiv = document.querySelector('#loading');
    toggleButton1.style.display = 'none'; // Initially hide the button
    toggleButton2.style.display = 'none'; // Initially hide the button
    toggleButton3.style.display = 'none'; // Initially hide the button
    toggleButton4.style.display = 'none';

    loadingDiv.style.display = 'block';
    const loadingInterval = setInterval(updateLoadingText, 500);

    const formData = new FormData(form);
    var errorboom = false;

    let data;
    try {
        const responsePromise = fetch('/', {
            method: 'POST',
            body: formData,
        });

        // Wait for both the response and the minimum 3 seconds
        const [response] = await Promise.all([responsePromise, sleep(3000)]);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        data = await response.json();
    } catch (error) {
        // Handle the error and display "오류 발생"
        console.error('Error:', error);
        data = { result: [['에러 발생']] };
        errorboom = true;
    } finally {
        // Stop updating and hide loading text
        clearInterval(loadingInterval);
        loadingDiv.style.display = 'none';
    }

    if (!errorboom) {
        toggleButton1.style.display = 'block';
        toggleButton2.style.display = 'block';
        toggleButton3.style.display = 'block'; // Show the Model 1 button
        toggleButton4.style.display = 'block';

        const chartContainer1 = document.querySelector('#chartContainer1');
        chartContainer1.style.display = 'none';
        drawBarChart(data.result);
    } else {
        const resultDiv = document.querySelector('#result');
        resultDiv.innerHTML = data.result;
    }
});

const toggleButton1 = document.getElementById('toggleButton1');
const toggleButton2 = document.getElementById('toggleButton2');
const toggleButton3 = document.getElementById('toggleButton3');
const toggleButton4 = document.getElementById('toggleButton4');
toggleButton1.style.display = 'none'; // Initially hide the button
toggleButton2.style.display = 'none'; // Initially hide the button
toggleButton3.style.display = 'none'; // Initially hide the button
toggleButton4.style.display = 'none'; // Initially hide the button

toggleButton1.addEventListener('click', () => {
    const chartContainer1 = document.querySelector('#chartContainer1');
    if (chartContainer1.style.display === 'none') {
        chartContainer1.style.display = 'block';
        drawBarChart(data.result);
        //toggleButton1.classList.add('active'); // Add "active" class to the button
    } else {
        chartContainer1.style.display = 'none';
        //toggleButton1.classList.remove('active'); // Remove "active" class from the button
    }
});

let myChart1; // Declare myChart outside of drawBarChart function

function drawBarChart(result) {
    const labels = [result[0][0], result[1][0]];
    const data = {
        labels: labels,
        datasets: [
            {
                label: '긍정문장 갯수',
                data: [result[0][1], result[1][1]],
                
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            },
            {
                label: '부정문장 갯수',
                data: [result[0][2], result[1][2]],
                
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }
        ]
    };

    // Destroy the previous chart
    if (myChart1) {
        myChart1.destroy();
    }

    const config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    stacked: true
                },
                x: {
                    stacked: true
                }
            }
        }
    };

    myChart1 = new Chart(
        document.getElementById('myChart1'),
        config
    );
}

function updateLoadingText() {
    const loadingDiv = document.querySelector('#loading');
    const loadingText = loadingDiv.textContent;
    if (loadingText.length < 6) {
        loadingDiv.textContent += '.';
    } else {
        loadingDiv.textContent = '분석중';
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const inputFile = document.querySelector('input[type="file"]');
inputFile.addEventListener('change', () => {
    const resultDiv = document.querySelector('#result');
    resultDiv.innerHTML = '';        
    const chartContainer1 = document.getElementById('chartContainer1');
    chartContainer1.style.display='none';
    const toggleButton1 = document.getElementById('toggleButton1');
    const toggleButton2 = document.getElementById('toggleButton2');
    const toggleButton3 = document.getElementById('toggleButton3');
    const toggleButton4 = document.getElementById('toggleButton4');
    toggleButton1.style.display = 'none'; // Initially hide the button
    toggleButton2.style.display = 'none'; // Initially hide the button
    toggleButton3.style.display = 'none'; // Initially hide the button
    toggleButton4.style.display = 'none'; // Initially hide the button
});