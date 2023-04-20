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
        const chartContainer2 = document.querySelector('#chartContainer2');
        chartContainer2.style.display = 'none';
        drawPieCharts(data.result2)
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
    const chartContainer2 = document.querySelector('#chartContainer2');
    const chartContainer3 = document.querySelector('#chartContainer3');
    const chartContainer4 = document.querySelector('#chartContainer4');
    chartContainer2.style.display = 'none';
    chartContainer3.style.display = 'none';
    chartContainer4.style.display = 'none';

    if (chartContainer1.style.display === 'none') {
        chartContainer1.style.display = 'block';
        drawBarChart(data.result);
        //toggleButton1.classList.add('active'); // Add "active" class to the button
    } else {
        chartContainer1.style.display = 'none';
        //toggleButton1.classList.remove('active'); // Remove "active" class from the button
    }
});

toggleButton2.addEventListener('click', () => {
    const chartContainer1 = document.querySelector('#chartContainer1');
    const chartContainer2 = document.querySelector('#chartContainer2');
    const chartContainer3 = document.querySelector('#chartContainer3');
    const chartContainer4 = document.querySelector('#chartContainer4');
    chartContainer1.style.display = 'none';
    chartContainer3.style.display = 'none';
    chartContainer4.style.display = 'none';

    if (chartContainer2.style.display === 'none') {
        chartContainer2.style.display = 'block';
        drawPieChart(data.result);
        //toggleButton1.classList.add('active'); // Add "active" class to the button
    } else {
        chartContainer2.style.display = 'none';
        //toggleButton1.classList.remove('active'); // Remove "active" class from the button
    }
});

let myChart1;
let myPieChart1;// Declare myChart outside of drawBarChart function
let myPieChart2;

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

// 모델2 파이그래프 1
function drawPieCharts(result) {
    const chartNames = [result[0][0], result[1][0]];
    const labels = ['매우부정', '부정', '중립', '긍정', '매우긍정'];

    const createPieConfig = (chartName, data, colors) => {
  return {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        label: chartName,
        data: data,
        backgroundColor: colors,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          callbacks: {
            label: function (context) {
              const label = context.label || '';
              const value = context.formattedValue || '';
              return `${label}: ${value}`;
            }
          }
        },
        legend: {
          display: false
        },
        title: {
          display: true,
          text: chartName,
          position: 'bottom'
        }
      },
    }
  };
};

    const colors = [  
    'rgba(76, 0, 76, 1)',
      'rgba(153, 0, 153, 1)',
        'rgba(153, 50, 204, 1)',
          'rgba(153, 102, 153, 1)',
            'rgba(229, 204, 229, 1)'];

    const pieChart1Config = createPieConfig(chartNames[0], result[0][1], colors);
    const pieChart2Config = createPieConfig(chartNames[1], result[1][1], colors);

    if (myPieChart1) {
        myPieChart1.destroy();
    }

    if (myPieChart2) {
        myPieChart2.destroy();
    }

    myPieChart1 = new Chart(
        document.getElementById('myPieChart1'),
        pieChart1Config
    );

    myPieChart2 = new Chart(
        document.getElementById('myPieChart2'),
        pieChart2Config
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
    const chartContainer2 = document.getElementById('chartContainer2');
    chartContainer2.style.display='none';
    const chartContainer3 = document.getElementById('chartContainer3');
    chartContainer3.style.display='none';
    const chartContainer4 = document.getElementById('chartContainer4');
    chartContainer4.style.display='none';
    const toggleButton1 = document.getElementById('toggleButton1');
    const toggleButton2 = document.getElementById('toggleButton2');
    const toggleButton3 = document.getElementById('toggleButton3');
    const toggleButton4 = document.getElementById('toggleButton4');
    toggleButton1.style.display = 'none'; // Initially hide the button
    toggleButton2.style.display = 'none'; // Initially hide the button
    toggleButton3.style.display = 'none'; // Initially hide the button
    toggleButton4.style.display = 'none'; // Initially hide the button
});