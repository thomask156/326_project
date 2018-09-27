const gulp = require("gulp");
const watch = require("gulp-watch");
const sequence = require("run-sequence");

const del = require("del");
const replace = require("gulp-replace");

const eol = require("gulp-eol");
const babel = require("gulp-babel");
const eslint = require("gulp-eslint");
const webpack = require("webpack-stream");

const sass = require("gulp-sass");
const autoprefixer = require("gulp-autoprefixer");
const concat = require("gulp-concat");
const cleanCSS = require("gulp-clean-css");

const cache = require("gulp-cache");
const imagemin = require("gulp-imagemin");


gulp.task("clean-js", () => {
    return del(["static/js/**", "!js"], {force:true});
});

gulp.task("clean-css", () => {
    return del(["static/css/**", "!css"], {force:true});
});

gulp.task("clean-fonts", () => {
    return del(["static/fonts/**", "!fonts"], {force:true});
});

gulp.task("clean-images", () => {
    return del(["static/img/**", "!img"], {force:true});
});

gulp.task("eol", ["clean-js"], () => {
    // Normalize EOL to Linux style (LF)
    return gulp.src("assets/js/*.js")
        .pipe(eol("\n"))
        .pipe(gulp.dest("static/js/es6/"));
});

gulp.task("eslint", ["clean-js", "eol"], () => {
    // Run ESLint
    return gulp.src(["static/js/es5/**/*.js", "static/js/es6/**/*.js"])
        .pipe(eslint())
        .pipe(eslint.format());
});

gulp.task("babel", ["clean-js", "eol", "eslint"], () => {
    // Convert to ES5
    return gulp.src("assets/js/**/*.js")
        .pipe(babel())
        .pipe(gulp.dest("static/js/es5"));
});

gulp.task("webpack", ["clean-js", "eol", "eslint", "babel"], () => {
	// Bundle
    return gulp.src("static/js/es5/**/*.js")
		.pipe(webpack({
    entry: "./static/js/es5/app.js",
    output:{
        filename: "argue.bundle.js"
    },
}))
		.pipe(gulp.dest("static/dist"));
});

gulp.task("sass", () => {
    return gulp.src("assets/sass/**/*.scss")
        .pipe(sass()) // Using gulp-sass
        .pipe(gulp.dest("static/css"));
});

gulp.task("css", ["sass"], () => {
	// bootstrap
    gulp.src("node_modules/bootstrap/dist/css/*.css")
		.pipe(gulp.dest("static/css/lib"));

	// font-awesome
    gulp.src("node_modules/font-awesome/css/*.css")
		.pipe(gulp.dest("static/css/lib"));

	// noty
    gulp.src("node_modules/noty/lib/*.css")
		.pipe(gulp.dest("static/css/lib"));

    gulp.src("node_modules/tempusdominus-bootstrap-4/build/css/*.min.css")
		.pipe(gulp.dest("static/css/lib"));

	// bootstrap-slider
    gulp.src("node_modules/bootstrap-slider/dist/css/*.min.css")
		.pipe(gulp.dest("static/css/lib"));

	// jquery chosen
    gulp.src("node_modules/chosen-js/chosen.min.css")
		.pipe(gulp.dest("static/css/lib"));

    // minify css
    return gulp.src(["static/css/lib/**/*.css"])
      .pipe(autoprefixer())
      .pipe(cleanCSS())
      .pipe(concat("argue.min.css"))
      .pipe(gulp.dest("static/dist"));
});

gulp.task("fonts", ["clean-fonts"], () => {
	// add fonts into css folder so they can be accessed by css in lib
    gulp.src("node_modules/font-awesome/fonts/*")
		.pipe(gulp.dest("static/css/fonts"));
    gulp.src("node_modules/bootstrap/dist/fonts/*")
		.pipe(gulp.dest("static/css/fonts"));
    gulp.src("assets/fonts/**/*")
		.pipe(gulp.dest("static/css/fonts"));

	// font-awesome
    gulp.src("node_modules/font-awesome/fonts/*")
		.pipe(gulp.dest("static/fonts"));

	// bootstrap
    gulp.src("node_modules/bootstrap/dist/fonts/*")
		.pipe(gulp.dest("static/fonts"));

    return gulp.src("assets/fonts/**/*")
        .pipe(gulp.dest("static/fonts"));
});

gulp.task("images", ["clean-images"], () => {
	// bootstrap-editable
    gulp.src("node_modules/bootstrap-editable/img/*")
		.pipe(gulp.dest("static/img"));

	// jquery chosen
    gulp.src("node_modules/chosen-js/*.png")
		.pipe(gulp.dest("static/dist"));

    return gulp.src("assets/img/**/*.+(png|jpg|jpeg|gif|svg)")
      .pipe(gulp.dest("static/img"));
});

gulp.task("default", () => {
    sequence("webpack", "css", "fonts", "images");
});

gulp.task("watch", () => {
    gulp.watch("assets/js/**/*.js", ["webpack"]);
    gulp.watch("assets/sass/**/*.scss", ["css"]);
    gulp.watch("assets/fonts/**/*.+(eot|svg|ttf|woff|otf|css)", ["fonts"]);
    gulp.watch("assets/img/**/*.+(png|jpg|jpeg|gif|svg)", ["images"]);
});