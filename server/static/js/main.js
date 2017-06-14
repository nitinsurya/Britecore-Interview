function checkFormValid(new_feature) {
    var flag = true;
    if($.trim(new_feature().title()) == '') {
        flag = false;
        $('.nf_title').addClass("is-invalid");
    } else {
        $('.nf_title').removeClass("is-invalid");
    }

    if($.trim(new_feature().description()) == '') {
        flag = false;
        $('.nf_desc').addClass("is-invalid");
    } else {
        $('.nf_desc').removeClass("is-invalid");
    }

    if(new_feature().client() == '') {
        flag = false;
        $('.nf_client').addClass("is-invalid");
    } else {
        $('.nf_client').removeClass("is-invalid");
    }

    if(new_feature().client_priority() == '' || new_feature().client_priority() < 0) {
        flag = false;
        $('.nf_client_priority').addClass("is-invalid");
    } else {
        $('.nf_client_priority').removeClass("is-invalid");
    }

    if(new_feature().date() == '') {
        flag = false;
        $('.nf_date').addClass("is-invalid");
    } else {
        $('.nf_date').removeClass("is-invalid");
    }

    if(new_feature().product_area() == '') {
        flag = false;
        $('.nf_pa').addClass("is-invalid");
    } else {
        $('.nf_pa').removeClass("is-invalid");
    }

    return flag;
}

function getFormattedDate() {
    var date = new Date();

    var month = (1 + date.getMonth()).toString();
    month = month.length > 1 ? month : '0' + month;

    var day = date.getDate().toString();
    day = day.length > 1 ? day : '0' + day;

    return month + '/' + day + '/' + date.getFullYear();
};