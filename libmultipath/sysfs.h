/*
 * sysfs.h
 */

#ifndef _LIBMULTIPATH_SYSFS_H
#define _LIBMULTIPATH_SYSFS_H

#ifdef DEBUG
# define dbg(format, args...) condlog(4, format, ##args)
#else
# define dbg(format, args...) do {} while (0)
#endif

int sysfs_init(char *path, size_t len);
void sysfs_cleanup(void);
void sysfs_device_set_values(struct sysfs_device *dev, const char *devpath,
			     const char *subsystem, const char *driver);
struct sysfs_device *sysfs_device_get(const char *devpath);
struct sysfs_device *sysfs_device_get_parent(struct sysfs_device *dev);
struct sysfs_device *sysfs_device_get_parent_with_subsystem(struct sysfs_device *dev, const char *subsystem);
void sysfs_device_put(struct sysfs_device *dev);
char *sysfs_attr_get_value(const char *devpath, const char *attr_name);
int sysfs_resolve_link(char *path, size_t size);
int sysfs_get_size (struct sysfs_device * dev, unsigned long long * size);
int sysfs_attr_set_value(const char *devpath, const char *attr_name,
			 const char *value);
#endif
