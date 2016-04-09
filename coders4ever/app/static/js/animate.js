var timeVariable = 0;
var numElems = 8;
var numBuckets = 10;
var elements = new Array(numElems);
var elementIds = new Array(numElems);
var moveDuration = 1000;
var bucketFull = new Array(numBuckets);
var back_audio = new Audio('static/audio/music2.wav');
back_audio.loop = true;
back_audio.play();

function setup() {
    for(var i=1; i<=numElems; i++) {
        var d = document.getElementById('elem' + i);
        elements[i-1] = d.innerHTML;
        d.style.left = 195 + (i-1)*120 +'px';
    }
    for(var i=1; i<=numBuckets; i++) {
        var d = document.getElementById('bucket' + i);
        d.style.left = 65 + (i-1)*120 +'px';
    }
}
setup();

function moveElementDown(element, bucket, bIndex) {
    setTimeout(function(){
        var b = document.getElementById("bucket" + bucket).getBoundingClientRect();
        var l = b.left;
        var m = b.top;
        $("#elem" + element).css('position','absolute').animate({
            left:l+15, top:m-60 - (bIndex)*80
        }, moveDuration);
        $("#elem" + element).css({
            backgroundColor:"orange",
        })
    }, timeVariable)
}
function moveElementUp(element, eIndex) {
    setTimeout(function(){	
        $("#elem" + element).css('position','absolute').animate({
            left:195 + (eIndex-1)*120 +'px', top:0
        }, moveDuration);
        $("#elem" + element).css({
            backgroundColor:"white",
        })
    }, timeVariable)
}

function countingSort(exp) {
    var output = new Array(numElems);
    var count = new Array(numBuckets);
    var buckets = [[], [], [], [], [], [], [], [], [], []];

    for(var i=0; i<numElems; i++) output[i] = 0;
    for(var i=0; i<numBuckets; i++) {
        count[i] = 0;
        bucketFull[i] = 1;
    }

    for(var i=0; i<numElems; i++) {
        var index = Math.floor(elements[i]/exp);
        var bucket = index%numBuckets;
        count[bucket] += 1
            moveElementDown(elementIds[i], bucket+1, bucketFull[bucket]);
        timeVariable += moveDuration;
        buckets[bucket].push(elementIds[i]);
        bucketFull[bucket] += 1;
    }

    for(var i=1; i<numBuckets; i++)
        count[i] += count[i-1];

    for(var i=numElems-1; i>=0; i--) {
        index = Math.floor(elements[i]/exp);
        var outputId = count[index%numBuckets]-1;
        output[outputId] = elements[i];
        count[index%numBuckets] -= 1;
    }
    var cnt = 1;
    for(var i=0; i<numBuckets; i++) {
        for(var j=0; j<bucketFull[i]-1; j++) {
            moveElementUp(buckets[i][j], cnt);
            timeVariable += moveDuration;
            elementIds[cnt - 1] = buckets[i][j];
            cnt += 1;
        }
    }
    for(var i=0; i<numElems; i++) {
        elements[i] = output[i];	
    }

}

function radixSort() {
    var max_element = Math.max.apply(null, elements);
    var exp = 1;
    for(var i=0; i<numElems; i++) elementIds[i] = i + 1;
    while(Math.floor(max_element/exp) > 0) {
        countingSort(exp);
        exp *= numBuckets;
    }
}
radixSort();
