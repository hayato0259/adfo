var example1 = new Vue({
    el: '#app',
    data: {
        files: [],
    },
    delimiters: ['${', '}'],
    methods: {
        change: function(e) {
            var file = e.target.files
            var reader = new FileReader()
            reader.readAsText(file[0]);
            reader.onload = function (ev) {
            }
            pos = this.files.length
            data = {
                name: file[0].name,
                path: file[0].path,
            }
            this.$set(this.files, pos, data)
        },
        clear: function() {
            document.getElementById("file").value = ""
        }
    }
})