#!/usr/bin/env python3
import os
import re
import sys
import glob
import shutil
import fnmatch
import argparse
import subprocess


def proto_refactor(proto_filename, namespace, namespace_path):
    """This method refactors a Protobuf file to import from a namespace
    that will map to the desired python package structure. It also ensures
    that the syntax is set to "proto2", since protoc complains without it.

    Args:
        proto_filename (str): the protobuf filename to be refactored
        namespace (str): the desired package name (i.e. "dropsonde.py2")
        namespace_path (str): the desired path corresponding to the package
                              name (i.e. "dropsonde/py2")
    """
    with open(proto_filename) as f:
        data = f.read()
        if not re.search('syntax = "proto2"', data):
            insert_syntax = 'syntax = "proto2";\n'
            data = insert_syntax + data
        substitution = 'import "{}/\\1";'.format(namespace_path)
        data = re.sub('import\s+"([^"]+\.proto)"\s*;', substitution, data)
        return data


def proto_refactor_files(dest_dir, namespace, namespace_path):
    """This method runs the refactoring on all the Protobuf files in the
    Dropsonde repo.

    Args:
        dest_dir (str): directory where the Protobuf files lives.
        namespace (str): the desired package name (i.e. "dropsonde.py2")
        namespace_path (str): the desired path corresponding to the package
                              name (i.e. "dropsonde/py2")
    """
    for dn, dns, fns in os.walk(dest_dir):
        for fn in fns:
            fn = os.path.join(dn, fn)
            if fnmatch.fnmatch(fn, '*.proto'):
                data = proto_refactor(fn, namespace, namespace_path)
                with open(fn, 'w') as f:
                    f.write(data)


def clone_source_dir(source_dir, dest_dir):
    """Copies the source Protobuf files into a build directory.

    Args:
        source_dir (str): source directory of the Protobuf files
        dest_dir (str): destination directory of the Protobuf files
    """
    if os.path.isdir(dest_dir):
        print('removing', dest_dir)
        shutil.rmtree(dest_dir)
    shutil.copytree(source_dir, dest_dir)


def protoc_command(lang, output_dir, proto_path, refactored_dir):
    """Runs the "protoc" command on the refactored Protobuf files to generate
    the source python/python3 files.

    Args:
        lang (str): the language to compile with "protoc"
                    (i.e. python, python3)
        output_dir (str): the output directory for the generated source files
        proto_path (str): the root protobuf build path in which to run "protoc"
        refactored_dir (str): the input directory of the Protobuf files
    """
    proto_files = glob.glob(os.path.join(refactored_dir, '*.proto'))
    cmd = ['protoc', '-I', proto_path, '--{}_out'.format(lang), output_dir]
    cmd.extend(proto_files)
    print(' '.join(cmd))
    p = subprocess.Popen(
        cmd, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin,
        cwd=proto_path)
    p.communicate()


def main():
    args = argparse.ArgumentParser()
    args.add_argument(
        '--source-dir', dest='source_dir', required=True,
        help='The source directory from which to copy the protobuf files')
    args.add_argument(
        '--namespace-path', dest='namespace_path', required=True,
        help='The namespace path structure under which to save the source '
             'files')
    args.add_argument(
        '--namespace-module', dest='namespace_module', required=True,
        help='The namespace module name to render into the generated source '
             'files')
    args.add_argument(
        '--lang', dest='language', required=True,
        help='The language to generate with "protoc" (i.e. python, python3)')
    args.add_argument(
        '--build-dir', dest='build_dir', default='build',
        help='The build directory in which to clone the Dropsonde repo and '
             'also the directory in which to refactor the Protobuf files')
    args.add_argument(
        '--output-dir', dest='output_dir', default='.',
        help='The directory in which to store the generated python/python3 '
             'files')
    args.add_argument('action', nargs='*', default=[])
    args = args.parse_args()

    source_dir = os.path.abspath(args.source_dir)
    output_dir = os.path.abspath(args.output_dir)
    build_dir = os.path.abspath(args.build_dir)
    proto_path = build_dir
    proto_dir = build_dir + '/' + args.namespace_path
    output_dir = output_dir
    namespace_module = args.namespace_module
    namespace_path = args.namespace_path
    language = args.language

    for action in args.action:
        if 'clone' == action:
            clone_source_dir(source_dir, proto_dir)
            print('created {}'.format(proto_dir))
        elif 'refactor' == action:
            proto_refactor_files(proto_dir, namespace_module, namespace_path)
            print('refactored {}'.format(proto_dir))
        elif 'protoc' == action:
            protoc_command(language, output_dir, proto_path, proto_dir)


if '__main__' == __name__:
    main()
