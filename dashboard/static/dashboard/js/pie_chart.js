// pie chart showing the distribution of tasks by priority

const pCtx = document.getElementById("pie_chart").getContext("2d");
const pie_chart = new Chart(pCtx, {
    type: "pie",
    data: {
        labels: pieLabels,
        datasets: [{
            label: "Number of Tasks",
            data: pieData,
            backgroundColor: [
                "rgb(35, 136, 35)",
                "rgb(255, 191, 0)",
                "rgb(210, 34, 45)"
            ]
        }]
    }
});