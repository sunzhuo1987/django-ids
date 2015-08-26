# Installation instructions #

  * Download the source svn checkout http://django-ids.googlecode.com/svn/trunk/ django-ids-read-only
  * Run python setup.py install

# Configuration #

**Rules configuration** _(Optional)_

Rules are taken from django ids svn repository. Using thi setting ensure that you use the latest avayable signature for rules. If you want a local copy of signatures file or develop your custom signatures file edit ids/core/settings.py

**Template configuration** _(Required for reports and Honeypot application)_

Add to your project template dir "ids/templates"