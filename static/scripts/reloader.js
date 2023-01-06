
function reloadCpu() {
    $.get("/api/get-cpu-usage-percent", function(data, status) { 
        $("#cpuBar").width(data.toString());
        $("#cpuBar").html(data.toString());
        $("#cpuBar").attr("aria-valuenow", data.toString());
    });
}

function reloadRam() {
    $.get("/api/get-ram-usage-percent", function(data, status){
        $("#ramBar").width(data.toString());
        $("#ramBar").html(data.toString());
        $("#ramBar").attr("aria-valuenow", data.toString());
    });
}

function reloadDisk() {
    $.get("/api/get-disk-usage-percent", function(data, status){
        $("#diskBar").width(data.toString());
        $("#diskBar").html(data.toString());
        $("#diskBar").attr("aria-valuenow", data.toString());
    });
}

window.onload = () => {
    setInterval(reloadCpu, 2000);
    setInterval(reloadRam, 2000);
    setInterval(reloadDisk, 2000);
}