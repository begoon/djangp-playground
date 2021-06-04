$.ajax({
    url: "api/echo", success: function (result) {
        console.table(result.message)
        $("#echo").html(result.message);
    }
})

$.ajax({
    url: "api/questions", success: function (result) {
        const questions = result.data.questions;
        const output = Object.values(questions).map(({ question, image }) => {
            return `${image}: ${question}`;
        });
        $("#questions").html(output.join('<br />'));
    }
})