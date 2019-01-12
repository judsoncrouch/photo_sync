from dirsync import sync
import win32api as win
import os
import click


def get_drive_names():
    drives = win.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    drive_map = {}
    for d in drives:
        drive_name = win.GetVolumeInformation(d)[0]
        drive_map[drive_name] = d
    return drive_map


def sync_raw_to_hdd(raw_dir, hdd):
    print "Syncing RAW to %s\n..." % hdd
    sync(raw_dir, hdd, "sync")
    print "     Complete\n"


def sync_catalog_to_backup(catalog, backup):
    print "Syncing Catalog to %s\n..." % backup
    sync(catalog, backup, "sync")
    print "     Complete\n"


def sync_hdd_to_backup(hdd, backup):
    print "Syncing %s to %s\n..." % (hdd, backup)
    sync(hdd, backup, "sync")
    print "     Complete\n"


@click.command()
@click.option('--raw', 'processes', flag_value='raw')
@click.option('--catalog', 'processes', flag_value='catalog')
@click.option('--all', 'processes', flag_value='all')
def main(processes):

    raw_dir = r"E:\Pictures\RAW"
    catalog_nm = "Catalog_JC"
    hdd_nm = "Photos_A1"

    backup_nm = "Photos_A1_Backup"

    try:

        drives = get_drive_names()
        hdd = drives[hdd_nm]
        backup = drives[backup_nm]
        catalog = drives[catalog_nm]


        if processes == 'raw':
            sync_raw_to_hdd(raw_dir, hdd)
            sync_hdd_to_backup(hdd, backup)
        elif processes == 'catalog':
            sync_catalog_to_backup(catalog, backup)
        else:
            sync_raw_to_hdd(raw_dir, hdd)
            sync_hdd_to_backup(hdd, backup)
            sync_catalog_to_backup(catalog, backup)

    except KeyError:
        print "Photo drives not found."

if __name__ == '__main__':
    main()