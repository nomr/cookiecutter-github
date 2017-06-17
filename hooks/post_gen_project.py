# -*- coding: utf-8 -*-
import os
import re
import shutil

from git import Repo


def fix_template_expansion(content, replacements):
    """
    fix template expansion after hook copy
    :param content: the duplicated hook content
    :param replacements: array of dictionaries
                         cookiecutter_key => template key expanded
    """
    for replacement in replacements:
        for key, to_be_replaced in replacement.items():
            replacement = chr(123) + chr(123) + \
                'cookiecutter.' + key + chr(125) + chr(125)
            content = content.replace(to_be_replaced, replacement)
    return content


def get_file_content(file):
    """
    get the content of a given file
    :param file: the file to get the content of
    """
    return open(file, 'r').read()


def set_file_content(file, content):
    """
    write content to file
    :param file: the file to rewrite its content
    :param content: content to write to the given file
    """
    return open(file, 'w').write(content)


def copy_hooks():
    if (not re.match(r'YES', '{{cookiecutter.copy_hooks if cookiecutter.copy_hooks is defined else "no"}}', re.I)):
        return
    if (re.match(r'^cookiecutter\-', '{{cookiecutter.project_slug}}')):
        hooksdir = os.getcwd() + '/hooks'
        posthook = hooksdir + '/post_gen_project.py'
        source = os.path.realpath(__file__)
        replacements = [
            {'project_slug': '{{cookiecutter.project_slug}}'},
            {'copy_hooks': '{{cookiecutter.copy_hooks if cookiecutter.copy_hooks is defined else "no"}}'},

            # project_name must be set after project_slug to prevent side
            # effects
            {'project_name': '{{cookiecutter.project_name}}'}
        ]

        if (not os.path.exists(hooksdir)):
            os.makedirs(hooksdir)
        shutil.copyfile(source, posthook)

        set_file_content(
            posthook,
            fix_template_expansion(
                get_file_content(posthook), replacements
            ) + "\n"
        )


def setup_git():
    ''' Initializes the git repository.

        It runs the equivalent of:
            git init
            git add .
            git commit -m 'Initial Commit'
            git tag -a VERSION
            git branch ck/template
    '''

    r = Repo.init()
    r.index.add(r.untracked_files)
    commit = r.index.commit("Initial Commit")

    tag = r.create_tag('{{cookiecutter.version}}')

    ck_tmpl_branch = r.create_head('ck/template')


if __name__ == "__main__":
    copy_hooks()
    setup_git()
