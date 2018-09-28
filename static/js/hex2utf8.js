var dec2utf8 = function (arr) {
    if (typeof arr === 'string') {
        return arr;
    }

    var unicodeString = '', _arr = arr;
    for (var i = 0; i < _arr.length; i++) {
        var one = _arr[i].toString(2);
        var v = one.match(/^1+?(?=0)/);

        if (v && one.length === 8) {
            var bytesLength = v[0].length;
            var store = _arr[i].toString(2).slice(7 - bytesLength);

            for (var st = 1; st < bytesLength; st++) {
                store += _arr[st + i].toString(2).slice(2)
            }

            unicodeString += String.fromCharCode(parseInt(store, 2));
            i += bytesLength - 1;
        } else {
            unicodeString += String.fromCharCode(_arr[i]);
        }
    }
    return unicodeString
};

function hex2a(hexx) {
    var hex = hexx.toString();//force conversion

    var str_list = [];
    for (var i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str_list.push(parseInt(hex.substr(i, 2), 16));

    return dec2utf8(str_list);
}


