`Hurricane Electric DNS <https://dns.he.net>`_ Library

Example usage
-------------

Create a configuration file with your username and password:

.. code-block:: ini

  certbot_dns_he:dns_he_user = Me
  certbot_dns_he:dns_he_pass = my HE password

and chmod it to ``600``:

.. code-block:: bash

  $ chmod 600 dns_he.ini
