function transform(line) {
    var values = line.split(',');
    var currentdate = new Date(); 
    var datetime =    currentdate.getFullYear() + "-"
                    + (currentdate.getMonth()+1)  + "-"
                    + currentdate.getDate() + "T"
                    + (currentdate.getHours()+5) + ":"  
                    + (currentdate.getMinutes()+30) + ":" 
                    + currentdate.getSeconds();

    var obj = new Object();
    obj.symbol = values[0];
    obj.name = values[1];
    obj.date = values[2];
    obj.open = values[3];
    obj.high = values[4];
    obj.low = values[5];
    obj.close  = values[6];
    obj.change= values[7];
    obj.changePercent= values[8];
    obj.label = values[9];
    obj.ingest_timestamp = datetime;

    var jsonstring = JSON.stringify(obj)

    return jsonstring;
}