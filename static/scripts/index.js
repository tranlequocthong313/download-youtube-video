function download(videoId) {
    var select = document.getElementById('quality-' + videoId)
    quality = select.value
    window.location.href = '/download/' + videoId + '/' + quality
}

function show_preview_video(videoId) {
    preview = document.getElementById('preview-' + videoId)
    preview_iframe = document.querySelector('#preview-' + videoId + ' iframe')
    console.log(preview_iframe.nodeName)

    preview.style.display = 'block'
    preview_iframe.src += videoId
    console.log(preview_iframe.src)
    console.log(videoId)
}