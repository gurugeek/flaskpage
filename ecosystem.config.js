module.exports = {
  apps : [{
    name: 'flask',
    script: './start.sh',

    // Options reference: https://pm2.io/doc/en/runtime/reference/ecosystem-file/
    args: 'one two',
    instances: 1,
    //exec_mode: 'cluster',
    merge_logs: true,
    autorestart: true,
    log_file: "logs/combined.outerr.log",
    out_file: "logs/out.log",
    error_file: "logs/err.log",
    log_date_format : "YYYY-MM-DD HH:mm Z",
    append_env_to_name: false,
  }],

};

