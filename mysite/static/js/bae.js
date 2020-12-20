const speechRecognition = window.webkitSpeechRecognition
const recognition = new speechRecognition();
const textBox1 = document.getElementById("#answer1");
const textBox2 = document.getElementById("#answer1");
const textBox3 = document.getElementById("#answer1");
const instruction = $("#instruction");

let content1 = '';
let content2 = '';
let content3 = '';

recognition.continuous = true;

recognition.onspeechend = () => {
    console.log("Speech End");
    recognition.start();
}

recognition.onerror = () => {
    console.log("On Error");
    recognition.start();
}

recognition.onresult = (event) => {
    const current = event.resultIndex;
    content1 = event.results[current][0].transcript;
    //c2
    content2 = event.results[current][1].transcript;
    content3 = event.results[current][2].transcript;
    
    //c3   
    textBox1.val(content1);
    //t2
    textBox2.val(content2);
    //t3
    textBox3.val(content3);
}

stt_start1 = () => {
  recognition.start();
}
stt_end1 = () => {
  recognition.stop();
}

stt_start2 = () => {
  recognition.start();
}
stt_end2 = () => {
  recognition.stop();
}

stt_start3 = () => {
  recognition.start();
}
stt_end3 = () => {
  recognition.stop();
}