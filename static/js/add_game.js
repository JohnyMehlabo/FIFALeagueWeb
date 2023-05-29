var goals_count = 0
var saves_count = 0

var add_event = () => {
    var event_type_selector = document.getElementById("event-type-selector")
    if (event_type_selector.value == 1){
        saves_count += 1
        var form = document.getElementById("events_form")
        var select_player_keeper = document.getElementById("player-select").cloneNode(true)
        select_player_keeper.setAttribute("name", `save-${saves_count}-keeper`)


        form.insertAdjacentHTML("beforeend", `
        <div class="mb-5 mx-3 event">
        <h2>Parada:</h2>
        </div>
        `)

        var events = document.getElementsByClassName("event")
        var last_event = events[events.length - 1]

        var keeper_text = document.createElement("h4")
        keeper_text.innerHTML = "Portero:"

        last_event.appendChild(keeper_text)
        last_event.appendChild(select_player_keeper)
    }
    else if (event_type_selector.value == 2) {
        goals_count +=1
        var form = document.getElementById("events_form")
        var select_player_scorer = document.getElementById("player-select").cloneNode(true)
        select_player_scorer.setAttribute("name", `goal-${goals_count}-scorer`)
        var select_player_assister = document.getElementById("player-select").cloneNode(true)
        select_player_assister.setAttribute("name", `goal-${goals_count}-assister`)
        var none_option = document.createElement("option")
        none_option.innerHTML = "Ninguno"
        select_player_assister.appendChild(none_option)
        
        form.insertAdjacentHTML("beforeend", `
        <div class="mb-5 mx-3 event">
        <h2>Gol:</h2>
        </div>
        `)


        var events = document.getElementsByClassName("event")
        var last_event = events[events.length - 1]

        var scorer_text = document.createElement("h4")
        scorer_text.innerHTML = "Marcador:"

        var assister_text = document.createElement("h4")
        assister_text.innerHTML = "Asistidor:"

        last_event.appendChild(scorer_text)
        last_event.appendChild(select_player_scorer)
        last_event.appendChild(assister_text)
        last_event.appendChild(select_player_assister)
    }
}