django-explain-commands
=======================

Are you tired to find where each command coming from? `django-explain-commands`
helps you to find which Django application provides each command.

Installation
------------

 1. Obtain source via git clone:

     git clone git://github.com/jellycrystal/django-explain-commands.git

 2. Install as regular package:

     python setup.py install

 3. Add `explain_commands` to `INSTALLED_APPS`.

Usage
-----
 
Run `python manage.py explain_commands` and enjoy.

Sample output:

    $ python manage.py explain_commands
    django.contrib.auth =>
        changepassword
        createsuperuser
    django.core =>
        cleanup
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        reset
        runfcgi
        runserver
        shell
        sql
        sqlall
        sqlclear
        sqlcustom
        sqlflush
        sqlindexes
        sqlinitialdata
        sqlreset
        sqlsequencereset
        startapp
        validate
    django_extensions =>
        clean_pyc
        compile_pyc
        create_app
        create_command
        create_jobs
        describe_form
        dumpscript
        export_emails
        generate_secret_key
        graph_models
        mail_debug
        passwd
        print_user_for_session
        reset_db
        runjob
        runjobs
        runprofileserver
        runscript
        runserver_plus
        set_fake_emails
        set_fake_passwords
        shell_plus
        show_templatetags
        show_urls
        sqldiff
        sync_media_s3
        syncdata
        unreferenced_files
    explain_commands =>
        explain_commands
    south =>
        convert_to_south
        datamigration
        graphmigrations
        migrate
        schemamigration
        startmigration
        syncdb
        test
        testserver
