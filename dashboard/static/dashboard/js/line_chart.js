// line chart showing the tasks due in the next 30 days

const lCtx = document.getElementById("line_chart").getContext("2d");
const line_chart = new Chart(lCtx, {
    type: "line",
    data: {
        labels: lineLabels,
        datasets: [{
            label: "Number of Tasks Due",
            data: lineData,
            backgroundColor: "rgba(75, 192, 192, 0.2)",
            borderColor: "rgba(75, 192, 192, 1)",
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});