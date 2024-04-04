# first create a virtual envirement for dependencies
sudo mkdir -p /opt
sudo python3 -m venv /usr/local/share/.dxf_thumbnailer_python_venv

# install all dependencies
sudo /usr/local/share/.dxf_thumbnailer_python_venv/bin/pip install ezdxf PyMuPdf pillow


# then copy all files to work
# copy thumbnailer entry
mkdir -p $HOME/.local/share/thumbnailers
cp dxf.thumbnailer $HOME/.local/share/thumbnailers/


# copy thumbnailer factory
sudo cp dxf-thumbnailer.py /usr/local/bin/
sudo chmod +x /usr/local/bin/dxf-thumbnailer.py

# NOW close all nautilus process
nautilus -q

# remove all cache images
rm -r $HOME/.cache/thumbnails

# update the database mime types
#update-mime-database $HOME/.local/share/mime/

# DONE!
echo "Installing done! please open nautilus and navigate to the folder with the LightBurn files"
echo "if any error, send your feedback"
