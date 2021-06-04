document.writeln('Javascript is talking');

const response = $.ajax({
    url: "api/", success: function (result) {
        $("#output").html(JSON.stringify(result));
    }
})