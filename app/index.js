"use strict";

const yosay = require("yosay");
const chalk = require("chalk");
const Generator = require("yeoman-generator");

const getModuleName = name => name.toLowerCase().replace(/[\s\.\-]+/, "_");
const pythonReleases = {
    "3.6": "3.6.12",
    "3.7": "3.7.9",
    "3.8": "3.8.5"
};

module.exports = class extends Generator {

    constructor(args, opts) {
        super(args, opts);

        this.argument("project_slug", { type: getModuleName, required: false });
    }

    async prompting() {
        this.log(
            yosay(
                "Let`s make cool backend based on Python3, asyncio/aiohttp and "+
                chalk.red("ultra fast") + " " + chalk.blue("uvloop") + "!"
            )
        );

        let prompts = [
            {
                type: "list",
                name: "python_version",
                message: "What versin of Python to use?",
                choices: Object.keys(pythonReleases)
            },
            {
                type: "confirm",
                name: "use_postgres",
                message: "Would you like to bootstap PostgreSQL database?",
                default: true,
                store: true
            },
            {
                type: "confirm",
                name: "use_redis",
                message: "Would you like to enable Redis support?",
                default: false,
                store: true
            },
            {
                type: "confirm",
                name: "use_docker",
                message: "Would you like to enable Docker support?",
                default: false,
                store: true
            },
            {
                type: "confirm",
                name: "use_gcp",
                message: "Would you like to enable Google Cloud Platform?",
                default: false,
                store: true
            },
            {
                type: "confirm",
                name: "use_heroku",
                message: "Would you like to enable Heroku cloud support?",
                default: false,
                store: true
            }

        ];

        if (!this.options.project_slug) {
            prompts = [
                {
                    type: "input",
                    name: "project_slug",
                    message: "What is the name of Python module?",
                    default: "app",
                },
                ...prompts
            ]
        }

        this.answers  = await this.prompt(prompts);
    }

    writing() {
        this.fs.copy(this.templatePath('config', '.*'), this.destinationPath());
        this.fs.copy(this.templatePath('config', 'setup.cfg'), this.destinationPath());

        if (this.answers.use_docker) {
            this.fs.copyTpl(
                this.templatePath('docker'),
                this.destinationPath(),
                this.answers
            );
        }

        if (this.answers.use_heroku) {
            this.fs.copy(this.templatePath('heroku', '*'), this.destinationPath());
        }

        this.fs.copyTpl(
            this.templatePath("src"),
            this.destinationPath("app"),
            this.answers
        );
        this.fs.copyTpl(
            this.templatePath("{Pipfile,Makefile,README.md}"),
            this.destinationPath(),
            this.answers
        );
    }
};
