/**
 * Created by maomao on 2020/4/23.
 */
Java.perform(function() {
    var cn = "java.util.Date";
    var target = Java.use(cn);
    if (target) {
        target.toLocaleString.implementation = function(dest) {
            var myArray=new Array()
            myArray[0] = "INTERESTED"  //INTERESTED & SENSITIVE
            myArray[1] = cn + "." + "toLocaleString";
            myArray[2] = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()).split('\n\tat');
            send(myArray);
            return this.toLocaleString.apply(this, arguments);
        };
    }
});