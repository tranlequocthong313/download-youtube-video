function download(videoId) {
    var select = document.getElementById('quality-' + videoId)
    var inputDestination = document.getElementById('destination')
    quality = select.value
    window.location.href = '/download?id=' + videoId + '&quality=' + quality + '&dest=' + inputDestination.value
}

function show_preview_video(videoId) {
    preview = document.getElementById('preview-' + videoId)
    preview_iframe = document.querySelector('#preview-' + videoId + ' iframe')

    preview.style.display = 'block'
    preview_iframe.src += videoId
}