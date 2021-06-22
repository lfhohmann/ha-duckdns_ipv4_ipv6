[![License](https://img.shields.io/github/license/lfhohmann/ha-duckdns_ipv4_ipv6?style=for-the-badge)](LICENSE)
[![HACS Badge](https://img.shields.io/badge/HACS-Default-blue.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
[![Maintainer](https://img.shields.io/badge/MAINTAINER-%40lfhohmann-blue?style=for-the-badge)](https://github.com/lfhohmann)
[![Community](https://img.shields.io/badge/COMMUNITY-FORUM-success?style=for-the-badge)](https://community.home-assistant.io)

# Home Assistant DuckDNS IPV4 and IPV6 updater

This is a custom component that can update both IPV4 and IPV6 entries of a [Duck DNS](https://www.duckdns.org/) subdomain, I developed this because the already integrated [Duck DNS Component](https://www.home-assistant.io/integrations/duckdns/) component is only able to update the IPV4 address over Duck DNS "autodetect mode" and I couldn't manage to get IPV6 working on the HassIO [Addon](https://github.com/home-assistant/hassio-addons/tree/master/duckdns). The code is pretty much a combination of the built-in [Duck DNS Component](https://www.home-assistant.io/integrations/duckdns/) and [DNS IP](https://www.home-assistant.io/integrations/dnsip/) with some extra features.

## Features

+ Doesn't need Docker nor HassIO.
+ Can be easily installed on any Home Assistant instance.
+ Can update both IPV4 and IPV6 addresses.
+ Three different IPV4 update modes: *(off, duckdns, nameserver)*.
+ Two different IPV6 update modes: *(off, nameserver)*.
+ Optionally, the user can specify the nameservers and host that he/she wants to use to resolve the IP addresses.

## Limitations

+ Home Assistant Core dependent *(It means that if Home Assistant Core stops working, this component will stop working too)*.
+ Currently, IPV6 can only be fetched via `nameserver` mode, *(maybe, more options can be added in the future)*.

## **Installation**

### **1. Before install:**

**Optional, but highly recommended steps!!**

1. **Backup!!!**
    + Backups are always a good idea, backup your current **Duck DNS** configuration *(If you already have one)*
    + HassIO users can simply create a Snapshot of their Home Assistant instance

1. **Disable** any components/addons that you are currently using to update your Duck DNS IP addresses *(If you have any)*
    + I believe that in most cases, this custom component should have no issues with other components/addons running in parallel, updating your Duck DNS IP addresses, so, **theoretically**, it should be safe to have more then one component/addon simultaneously. (**This hasn't been tested!**)
    + **But**, having more than one component/addon updating your Duck DNS IP addresses could make it hard to debug and figure out whether this component is working properly or not. So, if you want to have this custom component and other/s components/addons simultaneously on your setup, I would recommend you to disable all other components/addons before installing this and only enable then back once you have fully validated, that this custom component is working as it should.

### **2. Install Method A**: HACS

This is a regular HACS install from custom Github repository *(if you already know how to do it, you can probably skip the following steps)*

1. Copy this Github repository **[URL](https://github.com/lfhohmann/ha-duckdns_ipv4_ipv6)**
1. Open **HACS** on your Home Assistant interface
1. Open **Integrations**
1. Open the **menu/options** *(3 dots on the right upper conner)*
1. Select **"Custom Repositories"**
1. Paste the copied Github repository URL on **"Add custom repository URL"** field
1. Select **"Integration"** from the **"Category"** drop down menu
1. Click on the **"Add"** button
1. Click on the round **"Plus"** button *(Plus sign on the bottom right corner)*
1. Search for **"Duck DNS IPV4 and IPV6"**
1. Click on **"Install this repository on HACS"**
1. Click on **"Install"**
1. **Restart** your Home Assistant
1. **Done!** *(You still need to configure the component, check out the **[Configuration](https://github.com/lfhohmann/ha-duckdns_ipv4_ipv6#configuration)** section below)*

### **2. Install Method B**: Manual

1. Download the `custom_components` folder.
2. Copy the `duckdns_ipv4_ipv6` directory to the `custom_components` directory of your homeassistant installation. The `custom_components` directory resides within your homeassistant configuration directory.
**Note**: if the custom_components directory does not exist, you need to create it.
After a correct installation, your configuration directory should look like the following.

    ```text
    └── ...
    └── configuration.yaml
    └── custom_components
        └── duckdns_ipv4_ipv6
            └── __init__.py
            └── manifest.json
            └── services.yaml
    ```

### **3. Configuration**

Once the component has been installed, you need to configure it in order to make it work.
This component must be configured by manually editing the `configuration.yaml`:

**Note**: In orther for this component to work, you must already have signed up for an account on DuckDNS, registered a subdomain and have a valid Access Token.

#### A. Configuration example

```yaml
duckdns_ipv4_ipv6:
  access_token: YOUR_ACCESS_TOKEN
  domain: YOUR_SUBDOMAIN
  ipv4_mode: duckdns
  ipv6_mode: nameserver
```

#### B. Extended example

```yaml
duckdns_ipv4_ipv6:
  access_token: YOUR_ACCESS_TOKEN
  domain: YOUR_SUBDOMAIN
  ipv4_mode: duckdns
  ipv6_mode: nameserver
  hostname: "myip.opendns.com"
  ipv4_resolver: "208.67.222.222"
  ipv6_resolver: "2620:0:ccc::2"
```

## Configuration Variables

+ **access_token:** (string)(Required)
  + Your DuckDNS access token. Log in to the [DuckDNS website](https://www.duckdns.org/) and get one if you don't already have it.
+ **domain:** (string)(Required)
  + Your duckdns subdomain *(Without the `.duckdns.org` suffix)*.
+ **ipv4_mode:** (string)(Optional)
  + The method used to determine your external IPV4 address, options:
    + `"off"`: Will not update IPV4 address.
    + `"duckdns"`: Will use DuckDNS "autodetect mode" to determine your IPV4 address during the update request *(This is the fatest option).*
    + `"nameserver"`: Will use the `hostname` and the `ipv4_resolver` values to determine your IPV4 address and then update it on Duck DNS.
  + Default value: `"off"`
+ **ipv6_mode:** (string)(Optional)
  + The method used to determine your external IPV6 address, options:
    + `"off"`: Will not update IPV6 address.
    + `"nameserver"`: Will use the `hostname` and the `ipv6_resolver` values to determine your IPV6 address and then update it on Duck DNS.
  + Default value: `"off"`
  + **Note: There is no `"duckdns"` update method for IPV6 because Duck DNS does't provide one.**
+ **hostname:** (string)(Optional)
  + The hostname to be used to perform the nameserver DNS query.
  + Default value: `"myip.opendns.com"`
    + *This is a special hostname from [openDNS](https://www.opendns.com/) that resolves to your public IP.*
    + *You can find more options for hostnames bellow.*
  + **Note: The same `"hostname"` is used for both IPV4 and IPV6 address resolution.**
  + **Note: This is only used if the component is updating IPV4 and/or IPV6 via `"nameserver"` method.**
+ **ipv4_resolver:** (string)(Optional)
  + The nameserver/resolver used to determine your IPV4.
  + Default value: `"208.67.222.222"`
    + *This is the IPV4 address of an [openDNS](https://www.opendns.com/) nameserver.*
    + *You can find more options for IPV4 Resolvers bellow.*
  + **Note: This is only used if the component is updating IPV4 via `"nameserver"` method.**
+ **ipv6_resolver:** (string)(Optional)
  + The nameserver/resolver used to determine your IPV6.
  + Default value: `"2620:0:ccc::2"`
    + *This is the IPV6 address of an [openDNS](https://www.opendns.com/) nameserver.*
    + *You can find more options for IPV6 Resolvers bellow.*
  + **Note: This is ignored if you defined `ipv6_mode: "off"`.**

### Resolvers and Hostnames

Besides the default hostname and resolvers you can specify your own via the `hostname`, `ipv4_resolver` and `ipv6_resolver` parameters in the `configuration.yaml`. Bellow, you will find a list of known hostname and resolver combination. There might be other hostnames and resolvers that also work, but these are the ones I tested and managed to get working. (*As of today, they all work fine, but YMMV*).

+ Hostnames:
  + `o-o.myaddr.l.google.com`
    + IPV4 Resolvers:
      + `216.239.32.10`
      + `216.239.34.10`
      + `216.239.36.10`
      + `216.239.38.10`
    + IPV6 Resolvers:
      + `2001:4860:4802:32::a`
      + `2001:4860:4802:34::a`
      + `2001:4860:4802:36::a`
      + `2001:4860:4802:38::a`
  + `myip.opendns.com`
    + IPV4 Resolvers:
      + `208.67.222.222`
      + `208.67.220.220`
      + `208.67.222.220`
      + `208.67.220.222`
    + IPV6 Resolvers:
      + `2620:119:35::35`
      + `2620:119:53::53`
  + `whoami.akamai.net`
    + IPV4 Resolvers:
      + `193.108.88.1`

You must use resolvers that match your chosen hostname, otherwise, it won't work.

**Ex.:** If you choose the `o-o.myaddr.l.google.com` hostname, you must choose one of the following resolvers for IPV4: `216.239.32.10`,`216.239.34.10`,`216.239.36.10`,`216.239.38.10`. And one of the following resolvers for IPV6: `2001:4860:4802:32::a`,`2001:4860:4802:34::a`,`2001:4860:4802:36::a`,`2001:4860:4802:38::a`.

You can't combine the `whoami.akamai.net` hostname with `216.239.32.10` resolver for example.

# **DISCLAIMER**

This component has been running for several weeks flawlessly on my own Home Assistant installation **(X86_64 - Debian 10 - Home Assistant Supervised)**, updating both my IPV4 and IPV6 address periodically just like it's supposed to. If you follow all the instructions, setup things properly and validate your setup, you shouldn't have any issues with it.

### **BUT...**

This code can contain a few bugs here and there. **I am not responsible** for failures, bootloops, unresponsive/unbootable systems, hardware meltdown, **thermonuclear war**, or your house catching on fire beacuse you were not able to externally access your Home Assistant to turn off the oven. **YOU ARE FREE WILLINGLY CHOOSING** to install this component.

#

[![Buy me a coffe!](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/lfhohmann)
