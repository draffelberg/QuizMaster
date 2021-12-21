let answer = [];

fetch("https://draffelberg.github.io/QuizMaster/questions.json")
    .then(response => response.json())
    .then(questions => {

        for (a = 1; a <= 12; a++)
            document.getElementById("f" + a).innerHTML =    a + ". " + questions[a - 1].question;                             //Laden der Frage in HTML


        for (c = 1; c <= 12; c++) {                                                                             //Laden der Antwortmöglichkeiten in HTML
            for (j = 1; j <= 4; j++) {
                document.getElementById("f" + c + "_" + j).innerHTML = questions[c-1].answers[j-1];
       
            }
            
        }
        

        for (i = 0; i < 12; i++) {                                                                              //Speichern der richtigen Antworten im Array
            answer.push(questions[i].correct);
        }
        console.log(answer);
    })


    let input = document.querySelector("input[name='name']");                                               //func() disabled/enabled "Fertig"-Button
    let button = document.querySelector("input[id='submitbtn']");
    
    button.disabled = true; 
    
    input.addEventListener("change", stateHandle);
    
    function stateHandle() {
        if (document.querySelector("input[name='name']").value === "") {
            button.disabled = true; 
        } else {
            button.disabled = false; 
        }
    }


function submitAnswers() {                                                              //func() Button "Fertig"

    var numQuestions = 12;
    var score = 0;

    var name = document.querySelector('input[name="name"]').value;

    var rf1 = document.querySelector('input[name="rf1"]:checked');                  //Checkt ob Radio-Buttons geklickt worden sind
    var rf2 = document.querySelector('input[name="rf2"]:checked');      
    var rf3 = document.querySelector('input[name="rf3"]:checked');
    var rf4 = document.querySelector('input[name="rf4"]:checked');
    var rf5 = document.querySelector('input[name="rf5"]:checked');
    var rf6 = document.querySelector('input[name="rf6"]:checked');
    var rf7 = document.querySelector('input[name="rf7"]:checked');
    var rf8 = document.querySelector('input[name="rf8"]:checked');
    var rf9 = document.querySelector('input[name="rf9"]:checked');
    var rf10 = document.querySelector('input[name="rf10"]:checked');
    var rf11 = document.querySelector('input[name="rf11"]:checked');
    var rf12 = document.querySelector('input[name="rf12"]:checked');
    
    for (i = 1; i <= numQuestions; i++) {                                       //Alert-Ausgabe, falls eine Frage übersprungen worden ist

        if (eval("rf" + i) == null) {
            alert("Bitte beantworte Frage " + i + " noch");
            return false;
        }
    }

    
    
    for (i = 1; i <= numQuestions; i++) {                                       //Zählen der richtigen Antworten
        if (eval('rf' + i).value == answer[i - 1]) {
            score++;
        }
    }

                                                                                    //Ausgabe Punktzahl + Name

    var results = document.getElementById('resultat');                      
    results.innerHTML = '<h3>' + name + ', du hast <span>' + score + '</span> von <span>' + numQuestions + '</span> Punkten erzielt</h3>';
    return false;
}