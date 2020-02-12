/*
* library to process urls
* */
var x = (function (urlUtils) {

    function getUrlParameter(search, name) {
        name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)");
        var results = regex.exec(search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    //gets query parameter value by name
    urlUtils.getQueryParameter = function(urlString, queryParameter) {
        var url = new URL(urlString);
        if(window.URLSearchParams) {
            return new window.URLSearchParams(url.search).get(queryParameter);
        }else {
            return getUrlParameter(url, queryParameter);
        }
    };


}(window.urlUtils || (window.urlUtils = {})));