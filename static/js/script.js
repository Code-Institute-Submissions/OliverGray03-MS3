$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('.carousel').carousel();
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });
    $(".tooltipped").tooltip();
    $('select').formSelect();

    // Validation for drop down options//

    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

    //Adds an ingredient to a list in add recipe form//
    $("#add-ingredient").click(function () {
        var clone = $("#ingredient-container_0").clone();
        var ingredientContainers = $(".ingredient-container");
        clone.attr("id", "ingredient-container_" + ingredientContainers.length);
        clone.find("textarea").val("")
        $("#ingredients-container").append(clone);
        $("#remove-ingredient").show();
    });

    $("#remove-ingredient").click(function () {
        var ingredientContainers = $(".ingredient-container");
        ingredientContainers[ingredientContainers.length - 1].remove();

        if (ingredientContainers.length === 2) {
            $("#remove-ingredient").hide();
        }
    });


    //Adds a method step to a list in add recipe form//

    $("#add-method").click(function () {
        var clone = $("#method-container_0").clone();
        var methodContainers = $(".method-container");
        clone.attr("id", "method-container_" + methodContainers.length);
        clone.find("textarea").val("")
        $("#methods-container").append(clone);
        $("#remove-step").show();
    });

    $("#remove-step").click(function () {
        var methodContainers = $(".method-container");
        methodContainers[methodContainers.length - 1].remove();

        if (methodContainers.length === 2) {
            $("#remove-step").hide();
        }
    });

    $("#remove-step").hide();
    $("#remove-ingredient").hide();

    /*
    $("#confirm-password-error").hide();

    $("#confirm-password").blur(function () {
        debugger;
        if ($(this).val() != $("#password").val()) {
            //set custom error
            $("#confirm-password-error").show();
        }
    })

    $("#confirm-password").focus(function () {
        $("#confirm-password-error").hide();
    })*/
});