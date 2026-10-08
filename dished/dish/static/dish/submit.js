$(document).ready(function () {
    const hides = document.getElementsByClassName('hide')
    if (!($('input[type=checkbox][name=challenge]').is(':checked'))) {
        for (const hide of hides) {
            hide.style.display = "none"
        }
    }

    $('input[type=checkbox][name=challenge]').change(function () {
        if ($(this).is(':checked')) {
            for (const hide of hides) {
                hide.style.display = "block"
            }
        } else {
            for (const hide of hides) {
                hide.style.display = "none"
            }
        }
    });
});

// if ($(this).is(':checked')) {
//             $('.hide').each(function() {
//                 $(this).style.display = "block";
//             })
//         }
//         else {
//             console.log("test")
//             $('.hide').each(function() {
//                 $(this).style.display = "none";
//             })
//         }

// // $.getJSON("data/pastProj.json", () => {
// //     console.log("past projects loaded")
// // }).done((data) => {
// //     for (const proj of data) {
// //         const card = get_past_proj(proj);
// //         $('#pastProjList').append(card)
// //     }
//
function get_ingredient(i) {
    return `<div class="ingredient col-md-6">
                <div class="row form-group">
                    <div class="col-10">
                        <label>{{ form.ingredient${i}.label }} </label>
                        {{ form.ingredient${i} }}
                    </div>
                    <div class="col-2">
                        <label> </label>
                        {{ form.challenge${i} }}
                    </div>
                </div>
            </div>`
}


// const temp = document.currentScript.dataset
// console.log(temp)
// const form = temp.form
// console.log(form)

// $(function() {
//     // const form = document.currentScript
//     // console.log(form)
//     for (let i = 2; i < 11; i++) {
//         // console.log(i)
//         const ingredient = get_ingredient(i)
//         // console.log(ingredient)
//         // $('#ingredients').append(ingredient)
//     }
// })
