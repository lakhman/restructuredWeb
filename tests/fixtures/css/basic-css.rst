-----------------------------------
A heading to test the CSS directive
-----------------------------------

The css directive allows you to insert some css specific for that document.

It should be lifted into the head and outputted into the new block we create in extrahead.

.. css::

    /**
     * Our custom css lifted into the head
     */
    #custom-css {
      padding: 10px;
    }

Multiple ones should be added together (for includes for example).

.. css::

    /**
     * Our second custom css lifted into the head
     */
    #custom-css-2 {
      background-color: red;
    }

