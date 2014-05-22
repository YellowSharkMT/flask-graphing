/*global module*/
module.exports = function (grunt) {
    "use strict";
    var local_static = 'core/static/',
        bower = 'bower_components/',
        src = 'src/';

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        less: {
            local: {
                files: [
                    {expand: true, cwd: src + 'less', src: '**/*.less', dest: src + 'less', ext: '.build.css'}
                ]
            }
        },
        concat: {
            css: {
                src: [
                    src + 'less/*.build.css'
                ],
                dest: local_static + 'css/production.css'
            },
            js: {
                src: [
                    src + 'js/**/*.js'
                ],
                dest: local_static + 'js/production.js'
            }
        },
        watch: {
            templates: {
                files: 'core/templates/**/*.html',
                tasks: [],
                options: {
                    livereload: true
                }
            },
            less: {
                files: src + 'less/**/*.less',
                tasks: ['less', 'concat:css', 'clean:css'],
                options: {
                    livereload: true
                }
            },
            js: {
                files: src + 'js/**/*.js',
                tasks: ['concat:js'],
                options: {
                    livereload: true
                }
            }
        },
        clean: {
            css: [
                src + 'less/*.build.css'
            ]
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-less');

    grunt.registerTask('default', ['less', 'concat', 'clean', 'watch']);
};